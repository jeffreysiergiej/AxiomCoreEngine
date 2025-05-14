from src.axiomcore.os_kernel import os_boot_sequence

def test_os_boot_sequence(capsys):
    os_boot_sequence()
    captured = capsys.readouterr()
    assert "BOOTING" in captured.out
