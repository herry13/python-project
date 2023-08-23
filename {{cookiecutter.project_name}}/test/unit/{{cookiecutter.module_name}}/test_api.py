from {{ cookiecutter.module_name }}.app import main


def test_main(capsys):
    main()
    assert capsys.readouterr().out == "hello world!\n"
