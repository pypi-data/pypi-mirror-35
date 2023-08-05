import os
import shutil
import unittest
from dgen.tempdir import tempdir


class TestMake(unittest.TestCase):
    def tearDown(self):
        tempdir.remove()

    def test_creates_empty_tempdir(self):
        tempdir.make()
        assert os.path.exists(tempdir.path)
        assert not os.listdir(tempdir.path)     # assert is-empty

    def test_removes_existing_tempdir_with_its_content_and_creates_new_one(self):
        tempdir.make()
        os.mkdir(os.path.join(tempdir.path, 'aDir'))
        assert os.listdir(tempdir.path)         # assert is-not-empty

        tempdir.make()
        assert not os.listdir(tempdir.path)     # assert is-empty

    def test_removes_existing_file_that_has_name_of_tempdir_and_creates_tempdir(self):
        open(tempdir.dirname, 'w').close()
        assert os.path.isfile(tempdir.path)
        tempdir.make()
        assert os.path.isdir(tempdir.path)


class TestRemove(object):
    def test_removes_file_that_has_name_of_tempdir(self):
        open(tempdir.dirname, 'w').close()
        assert os.path.isfile(tempdir.path)
        tempdir.remove()
        assert not os.path.exists(tempdir.path)

    def test_removes_tempdir(self):
        tempdir.make()
        tempdir.remove()
        assert not os.path.exists(tempdir.path)


class TestCopyFiles(unittest.TestCase):
    def setUp(self):
        self.dst_dir = os.path.abspath('dst_dir')

    def tearDown(self):
        shutil.rmtree(self.dst_dir)
        tempdir.remove()

    def test_copies_files_from_tempdir_to_existing_dir(self):
        tempdir.make()

        file1 = 'file1'
        file2 = 'file2'
        open(os.path.join(tempdir.path, file1), 'w').close()
        open(os.path.join(tempdir.path, file2), 'w').close()

        os.mkdir(self.dst_dir)

        tempdir.copy_files([file1, file2], self.dst_dir)

        assert os.path.isfile(os.path.join(self.dst_dir, file1))
        assert os.path.isfile(os.path.join(self.dst_dir, file2))

    def test_copies_files_from_tempdir_to_not_existing_dir(self):
        tempdir.make()

        file1 = 'file1'
        file2 = 'file2'
        open(os.path.join(tempdir.path, file1), 'w').close()
        open(os.path.join(tempdir.path, file2), 'w').close()

        tempdir.copy_files([file1, file2], self.dst_dir)

        assert os.path.isfile(os.path.join(self.dst_dir, file1))
        assert os.path.isfile(os.path.join(self.dst_dir, file2))

    def test_copies_files_from_tempdir_to_not_existing_path(self):
        tempdir.make()

        file1 = 'file1'
        file2 = 'file2'
        open(os.path.join(tempdir.path, file1), 'w').close()
        open(os.path.join(tempdir.path, file2), 'w').close()

        dst_dir_child = os.path.join(self.dst_dir, 'dst_dir_child')

        tempdir.copy_files([file1, file2], dst_dir_child)

        assert os.path.isfile(os.path.join(dst_dir_child, file1))
        assert os.path.isfile(os.path.join(dst_dir_child, file2))
