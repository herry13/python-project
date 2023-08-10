from {{ cookiecutter.module_name }}.main import main


def test_main(capsys):
    main()
    assert capsys.readouterr().out == "hello world!\n"
