from apps.sample.main import main


def test_main_prints_greeting(capsys):
    main()
    assert "Hello from sandbox!" in capsys.readouterr().out
