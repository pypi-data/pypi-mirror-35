from etp import EnhancedThreadpool
import time


class TestClass(object):
    def test_one(self):
        t = EnhancedThreadpool(time.sleep, 3)
        t.execute_async(30)
        assert t.get_work_count() == 1

    def test_two(self):
        t = EnhancedThreadpool(time.sleep, 3)
        t.execute_async(1)
        time.sleep(3)
        assert t.get_work_count() == 0