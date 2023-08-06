from multiprocessing import cpu_count, Manager, Process
from time import sleep


class Parallelizer:

    def __init__(
            self,
            *,
            target: 'function',
            args: list,
            enable_results: bool,
            auto_proc_count: bool,
            max_proc_count: int):
        """
        Constructor, no positional args needed, all named args required
        :param target: function: target for multiple processes
        :param args: list: args to be passed to each instance of target. 
            Target function must accept an individual arg as its first param 
            (though can be tuple/dict/any encapsulating data structure).
        :param enable_results: bool: enables/disables a managed proxylist
            to hold data from the target function.  Disable if you only need 
            the target func to run and do not need it to modify/persist data.  
            If enabled, passes managed proxylist to target func, therefore
            target func must accept the list as its second param.
        :param auto_proc_count: bool: True=let class determine number of
            processes to use - calculates based on number of cores installed
            and number of operations to be performed.  
            False=use max_proc_count number of processes.
        :param max_proc_count: int: max number of processes to be spawned
            simultaneously
        """
        self.target = target
        self.args = args
        self.enable_results = enable_results

        self.__proc_count = 0
        self.__cpu_count = cpu_count()

        self.__iterations = len(args)
        self.__processes = []
        self.__incoming = 0
        self.__running = 0
        self.__finished = [False for _ in range(len(args))]

        self.__set_proc_count(auto_proc_count, max_proc_count)

    def run(self):
        """
        Runs the target function, manages core/process count/activity
        :return: list: results, unpackaged from manager.list proxy.
            Recommended to enclose results in target function in tuples 
            or other data structures before appending to the proxy list 
            to avoid race conditions.
        """
        if self.enable_results:
            return self.__run_managed()
        else:
            self.__run_unmanaged()

    def __run_managed(self):
        """
        Configures process manager and runs procs
        :return: List: converted from ProxyList
        """

        with Manager() as manager:
            results = manager.list()

            self.__generate_procs(results)
            self.__run_procs()
            self.__finalize_procs()

            results = list(results)

            return results

    def __run_unmanaged(self):
        """
        Runs data-unmanaged procs - for when you just want to run in
        parallel and don't need 'return' data
        :return: nothing
        """

        self.__generate_procs()
        self.__run_procs()
        self.__finalize_procs()

    def __run_procs(self):
        """
        Runs processes, prints self on exception and re-raises exception
        :return: nothing
        """

        try:
            while self.__incoming < self.__iterations:
                # sleep reduces the CPU impact of this 'manager loop'
                sleep(1 / 100)
                self.__mark_finished_procs()
                self.__spawn_available_procs()
        except Exception as e:
            print(self)
            raise e

    def __set_proc_count_auto(self, max_procs: int):
        """
        Calculates optimal proc_count to reduce ram usage, but also
        reduce wait time when only a single thread may be running
        :param max_procs: int: max procs to allow simultaneously
        :return: None
        """
        if (self.__iterations <= self.__cpu_count
                and self.__iterations <= max_procs):
            self.__proc_count = self.__iterations
        elif max_procs <= self.__cpu_count:
            self.__proc_count = max_procs
        else:
            self.__proc_count = self.__cpu_count
            for i in range(self.__cpu_count, max_procs + 1):
                if self.__iterations % i == 0:
                    self.__proc_count = i
                    break

        print(f'Using {self.__proc_count} processes')

    def __set_proc_count_manual(self, count: int):
        """
        Manually set the proc count.  Use with care when using
        very large counts.  Higher count = higher ram usage.
        :param count: int: number of procs to run simultaneously
        :return: None
        """
        self.__proc_count = count

    def __validate_proc_count(self, count: int):
        """
        Throws ValueError if count < 1
        :return: None
        """
        if count < 1:
            raise ValueError('Number of processes must be > 0')
        elif isinstance(count, bool) or not isinstance(count, int):
            raise ValueError('Number of processes must be an integer')

    def __set_proc_count(self, auto_proc_count: bool, max_proc_count: int):
        """
        Sets proc count based on auto_procs true/false
        :param auto_proc_count: bool: use auto proc count?
        :param max_proc_count: int: max num of procs to run simultaneously
        :return: None
        """
        self.__validate_proc_count(max_proc_count)

        if auto_proc_count:
            self.__set_proc_count_auto(max_proc_count)
        else:
            self.__set_proc_count_manual(max_proc_count)

    def __generate_procs(self, managed_results=None):
        """
        Generates a list of procs ready for starting
        :param managed_results: proxy manager.list: to store 
            data from target func
        :return: None
        """
        if managed_results is not None:
            for arg in self.args:
                self.__processes.append(Process(
                    target=self.target,
                    args=(arg, managed_results)
                ))
        else:
            for arg in self.args:
                self.__processes.append(Process(
                    target=self.target,
                    args=(arg,)
                ))

    def __spawn_available_procs(self):
        """
        Spawns procs if the number of currently running procs is
        less than the number of max_procs defined
        :return: None
        """
        if self.__running < self.__proc_count:
            self.__processes[self.__incoming].start()
            self.__incoming += 1
            self.__running += 1

    def __mark_finished_procs(self):
        """
        Checks currently running procs for status, marks finished
        :return: None
        """
        for i in range(self.__incoming):
            if not self.__processes[i].is_alive():
                if not self.__finished[i]:
                    self.__running -= 1
                    self.__finished[i] = True

    def __finalize_procs(self):
        """
        Finalizes procs/waits on remaining running procs
        :return: None
        """
        [process.join() for process in self.__processes]
        self.__mark_finished_procs()

    def __str__(self):
        stats = f'\n' \
                f'Target function:   {self.target.__name__}\n' \
                f'Number of iters:   {self.__iterations}\n' \
                f'Number of threads: {self.__proc_count}\n' \
                f'Number of procs:   {len(self.__processes)}\n' \
                f'Current incoming:  {self.__incoming}\n' \
                f'Current running:   {self.__running}\n' \
                f'Current finished:  {sum(self.__finished)}' \
                f'\n'

        return stats

    def __repr__(self):
        return self.__str__()
