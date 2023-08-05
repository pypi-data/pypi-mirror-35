from multiprocessing.pool import ThreadPool


class EnhancedThreadpool(ThreadPool):
    def __init__(self, pool_method, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__work_count = 0
        self.pool_method = pool_method

    def get_work_count(self):
        return self.__work_count

    def adjust_args(self, args, kwargs):
        def get_new_callback(orig_callback):
            def new_callback(return_result):
                try:
                    return orig_callback(return_result)
                finally:
                    self.__work_count -= 1  # work complete

            return new_callback

        def get_new_err_callback(orig_err_callback):
            def new_err_callback(err):
                try:
                    return orig_err_callback(err)
                finally:
                    self.__work_count -= 1  # work errored out, so basically work complete
            return new_err_callback

        if len(args) > 2:
            args[2] = get_new_callback(args[2])
        elif 'callback' in kwargs:
            kwargs['callback'] = get_new_callback(kwargs['callback'])
        else:
            kwargs['callback'] = get_new_callback(lambda r: None)

        if len(args) > 3:
            args[3] = get_new_err_callback(args[3])
        elif 'error_callback' in kwargs:
            kwargs['error_callback'] = get_new_err_callback(kwargs['error_callback'])
        else:
            kwargs['error_callback'] = get_new_err_callback(lambda e: None)

        return args, kwargs

    def apply_async(self, *args, **kwargs):
        (args, kwargs) = self.adjust_args(args, kwargs)
        self.__work_count += 1
        return super().apply_async(self.pool_method, *args, **kwargs)

    def execute_async(self, *args, **kwargs):
        return self.apply_async(args, kwargs)

    def apply(self, *args, **kwargs):
        self.__work_count += 1
        try:
            return super().apply(self.pool_method, *args, **kwargs)
        finally:
            self.__work_count -= 1
            
    def execute(self, *args, **kwargs):
        return self.apply(args, kwargs)
