from src.axiomcore.os_kernel import AxiomOSKernel

def test_task_execution():
    log = []
    kernel = AxiomOSKernel()
    kernel.schedule_task(lambda: log.append("ran"))
    kernel.run_all()
    assert log == ["ran"]
