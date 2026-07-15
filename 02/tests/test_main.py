from src.main import DocumentEditor
import pytest

class TestDocumentEditor:


    def test_write(self):
        editor = DocumentEditor()
        editor.write('Some text here!')
        assert editor.content == 'Some text here!'

    def test_clear(self):
        editor = DocumentEditor()
        editor.write('Some text here!')
        editor.clear()
        assert editor.is_empty()

    def test_get_last_content(self):
        editor = DocumentEditor()
        expected_last_content = 'Some new line here'


        editor.clear()
        editor.write(expected_last_content)


        last_content = editor.get_last_content()      

        error_msg = (f'\n=================\n'
                     f'expected_last_content:\n'
                     f'{expected_last_content}'
                     f'\n=================\n'
                     f'last_content:\n'
                     f'{last_content}'
                     f'\n=================\n')

        assert last_content == expected_last_content, error_msg
        
        if last_content != expected_last_content:
            pytest.fail(error_msg)

    def test_raise_error_if_no_history(self):
        editor = DocumentEditor()
        with pytest.raises(ValueError, match='No document history*'):
            editor.get_last_content()

    def test_multiple_scenarios_at_once(self):
        editor = DocumentEditor()

        assert editor.is_empty()
        assert len(editor.history) == 0

        editor.clear()
        assert editor.is_empty()
        assert len(editor.history) == 1

        editor.write('Some line of text. ')
        editor.write('Next sentence here!')

        assert editor.content == 'Some line of text. Next sentence here!'
        assert editor.is_empty()

    def test_dummy(self):
        assert True

