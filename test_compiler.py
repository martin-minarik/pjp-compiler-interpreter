import filecmp
import tempfile

from compiler import compile_code


def check_sample(code_filepath: str, reference_filepath: str) -> bool:
    instructions = compile_code(code_filepath)
    with tempfile.NamedTemporaryFile(mode="w", delete_on_close=False) as temp_file:
        temp_file.write(instructions)
        temp_file.close()

        filecmp.clear_cache()
        return filecmp.cmp(temp_file.name, reference_filepath, shallow=False)


def test_sample1() -> None:
    assert check_sample(
        code_filepath=r"samples/PLC_t1.in.txt",
        reference_filepath=r"samples/PLC_t1.out.txt",
    )


def test_sample2() -> None:
    assert check_sample(
        code_filepath=r"samples/PLC_t2.in.txt",
        reference_filepath=r"samples/PLC_t2.out.txt",
    )


def test_sample3() -> None:
    assert check_sample(
        code_filepath=r"samples/PLC_t3.in.txt",
        reference_filepath=r"samples/PLC_t3.out.txt",
    )
