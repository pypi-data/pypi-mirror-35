import ctypes
import os
import gzip
import shutil
import tempfile

PATH = os.path.dirname(__file__)
cgaddag_path = os.path.join(PATH, "libcgaddag.so")
cgaddag = ctypes.cdll.LoadLibrary(cgaddag_path)


class cResult(ctypes.Structure):
    pass

cResult._fields_ = [("str", ctypes.c_char_p),
                    ("next", ctypes.POINTER(cResult))]


class cGADDAG(ctypes.Structure):
    _fields_ = [("cap", ctypes.c_uint),
                ("num_words", ctypes.c_uint),
                ("num_nodes", ctypes.c_uint),
                ("num_edges", ctypes.c_uint),
                ("edges", ctypes.POINTER(ctypes.c_uint)),
                ("letter_sets", ctypes.POINTER(ctypes.c_uint))]


cgaddag.gdg_create.restype = ctypes.POINTER(cGADDAG)

cgaddag.gdg_save.restype = ctypes.c_bool
cgaddag.gdg_save.argtypes = [ctypes.POINTER(cGADDAG),
                             ctypes.c_char_p]

cgaddag.gdg_load.restype = ctypes.POINTER(cGADDAG)
cgaddag.gdg_load.argtypes = [ctypes.c_char_p]

cgaddag.gdg_add_word.restype = ctypes.c_void_p
cgaddag.gdg_add_word.argtypes = [ctypes.POINTER(cGADDAG),
                                 ctypes.c_char_p]

cgaddag.gdg_has.restype = ctypes.c_bool
cgaddag.gdg_has.argtypes = [ctypes.POINTER(cGADDAG),
                            ctypes.c_char_p]

cgaddag.gdg_starts_with.restype = ctypes.POINTER(cResult)
cgaddag.gdg_starts_with.argtypes = [ctypes.POINTER(cGADDAG),
                                    ctypes.c_char_p]

cgaddag.gdg_contains.restype = ctypes.POINTER(cResult)
cgaddag.gdg_contains.argtypes = [ctypes.POINTER(cGADDAG),
                                 ctypes.c_char_p]

cgaddag.gdg_ends_with.restype = ctypes.POINTER(cResult)
cgaddag.gdg_ends_with.argtypes = [ctypes.POINTER(cGADDAG),
                                  ctypes.c_char_p]

cgaddag.gdg_edges.restype = ctypes.c_void_p
cgaddag.gdg_edges.argtypes = [ctypes.POINTER(cGADDAG),
                              ctypes.c_uint,
                              ctypes.c_char_p]

cgaddag.gdg_letter_set.restype = ctypes.c_void_p
cgaddag.gdg_letter_set.argtypes = [ctypes.POINTER(cGADDAG),
                                   ctypes.c_uint,
                                   ctypes.c_char_p]

cgaddag.gdg_is_end.restype = ctypes.c_bool
cgaddag.gdg_is_end.argtypes = [ctypes.POINTER(cGADDAG),
                               ctypes.c_uint,
                               ctypes.c_char]

cgaddag.gdg_follow_edge.restype = ctypes.c_uint
cgaddag.gdg_follow_edge.argtypes = [ctypes.POINTER(cGADDAG),
                                    ctypes.c_uint,
                                    ctypes.c_char]

cgaddag.gdg_destroy.restype = ctypes.c_void_p
cgaddag.gdg_destroy.argtypes = [ctypes.POINTER(cGADDAG)]

cgaddag.gdg_destroy_result.restype = ctypes.c_void_p
cgaddag.gdg_destroy_result.argtypes = [ctypes.POINTER(cResult)]


class Node():
    """
    A node in a GADDAG.
    """
    def __init__(self, gdg, node):
        self.node = node
        self.gdg = gdg

    def __str__(self):
        return "[{}] {}".format(", ".join(sorted([edge for edge in self])),
                                self.letter_set)

    def __len__(self):
        return len(self.edges)

    def __iter__(self):
        for char in self.edges:
            yield char

    def __contains__(self, char):
        char = char.lower()
        return char in self.edges

    def __getitem__(self, char):
        char = char.lower()
        next_node = cgaddag.gdg_follow_edge(self.gdg, self.node,
                                            char.encode("ascii"))

        if not next_node:
            raise KeyError(char)

        return Node(self.gdg, next_node)

    def __eq__(self, other):
        if type(other) is not type(self):
            return NotImplemented

        if self.letter_set != other.letter_set or self.edges != other.edges:
            return False

        for child in self:
            if self[child] != other[child]:
                return False

        return True

    @property
    def edges(self):
        """
        Return the edges of this node.
        """
        edge_str = ctypes.create_string_buffer(27)

        cgaddag.gdg_edges(self.gdg, self.node, edge_str)

        return [char for char in edge_str.value.decode("ascii")]

    @property
    def letter_set(self):
        """
        Return the letter set of this node.
        """
        end_str = ctypes.create_string_buffer(27)

        cgaddag.gdg_letter_set(self.gdg, self.node, end_str)

        return [char for char in end_str.value.decode("ascii")]

    def is_end(self, char):
        """
        Return `True` if this `char` is part of this node's letter set,
        `False` otherwise.
        """
        char = char.lower()

        return bool(cgaddag.gdg_is_end(self.gdg, self.node, char.encode("ascii")))

    def follow(self, chars):
        """
        Traverse the GADDAG to the node at the end of the given characters.

        Args:
            chars: An string of characters to traverse in the GADDAG.

        Returns:
            The Node which is found by traversing the tree.
        """
        chars = chars.lower()

        node = self.node
        for char in chars:
            node = cgaddag.gdg_follow_edge(self.gdg, node, char.encode("ascii"))
            if not node:
                raise KeyError(char)

        return Node(self.gdg, node)


class GADDAG():
    """
    A data structure that allows extremely fast searching of words.
    """
    def __init__(self, words=None):
        self.gdg = cgaddag.gdg_create().contents

        if words:
            if type(words) is str:
                raise TypeError("Input must be an iterable of strings")

            for word in words:
                self.add_word(word)

    def __len__(self):
        return self.gdg.num_words

    def __contains__(self, word):
        word = word.lower()

        return cgaddag.gdg_has(self.gdg, word.encode(encoding="ascii"))

    def __iter__(self):
        for word in self.ends_with(""):
            yield word

    def __eq__(self, other):
        if type(other) is not type(self):
            return NotImplemented

        if len(self) != len(other):
            return False

        return self.root == other.root

    def __del__(self):
        cgaddag.gdg_destroy(self.gdg)

    @property
    def root(self):
        """
        Returns the root node of the GADDAG.
        """
        return Node(self.gdg, 0)

    def save(self, path, compressed=True, exist_ok=False):
        """
        Save the GADDAG to file.

        Args:
            path: path to save the GADDAG to.
            compressed: compress the saved GADDAG using gzip.
            exist_ok: overwrite existing file at `path`.
        """
        path = os.path.expandvars(os.path.expanduser(path))
        if os.path.isfile(path) and not exist_ok:
            raise OSError(17, os.strerror(17), path)

        if os.path.isdir(path):
            path = os.path.join(path, "out.gdg")

        if compressed:
            gz_path = path
            tmp = tempfile.NamedTemporaryFile(delete=False)
            path = tmp.name
            tmp.close()

        suc = cgaddag.gdg_save(self.gdg, path.encode("ascii"))
        if not suc:
            errno = ctypes.c_int.in_dll(ctypes.pythonapi, "errno").value
            raise OSError(errno, os.strerror(errno), path)

        if compressed:
            with open(path, "rb") as f_in:
                with gzip.open(gz_path, "wb") as f_out:
                    shutil.copyfileobj(f_in, f_out)

            os.remove(path)

    def load(self, path):
        """
        Load a GADDAG from file, replacing the words currently in this GADDAG.

        Args:
            path: path to saved GADDAG to be loaded.
        """
        path = os.path.expandvars(os.path.expanduser(path))

        compressed = False
        with gzip.open(path, "rb") as gzf:
            with tempfile.NamedTemporaryFile(delete=False) as f:
                try:
                    shutil.copyfileobj(gzf, f)
                    path = f.name
                    compressed = True
                except OSError as e:
                    pass

        gdg = cgaddag.gdg_load(path.encode("ascii"))
        if not gdg:
            errno = ctypes.c_int.in_dll(ctypes.pythonapi, "errno").value
            raise OSError(errno, os.strerror(errno), path)

        if compressed:
            os.remove(path)

        self.__del__()
        self.gdg = gdg.contents

    def starts_with(self, prefix):
        """
        Find all words starting with a prefix.

        Args:
            prefix: A prefix to be searched for.

        Returns:
            A set of all words found.
        """
        prefix = prefix.lower()
        found_words = []

        res = cgaddag.gdg_starts_with(self.gdg, prefix.encode(encoding="ascii"))
        tmp = res

        while tmp:
            word = tmp.contents.str.decode("ascii")
            found_words.append(word)
            tmp = tmp.contents.next

        cgaddag.gdg_destroy_result(res)
        return found_words

    def contains(self, sub):
        """
        Find all words containing a substring.

        Args:
            sub: A substring to be searched for.

        Returns:
            A set of all words found.
        """
        sub = sub.lower()
        found_words = set()

        res = cgaddag.gdg_contains(self.gdg, sub.encode(encoding="ascii"))
        tmp = res

        while tmp:
            word = tmp.contents.str.decode("ascii")
            found_words.add(word)
            tmp = tmp.contents.next

        cgaddag.gdg_destroy_result(res)
        return list(found_words)

    def ends_with(self, suffix):
        """
        Find all words ending with a suffix.

        Args:
            suffix: A suffix to be searched for.

        Returns:
            A set of all words found.
        """
        suffix = suffix.lower()
        found_words = []

        res = cgaddag.gdg_ends_with(self.gdg, suffix.encode(encoding="ascii"))
        tmp = res

        while tmp:
            word = tmp.contents.str.decode("ascii")
            found_words.append(word)
            tmp = tmp.contents.next

        cgaddag.gdg_destroy_result(res)
        return found_words

    def add_word(self, word):
        """
        Add a word to the GADDAG.

        Args:
            word: A word to be added to the GADDAG.
        """
        word = word.lower()

        if not (word.isascii() and word.isalpha()):
            raise ValueError("Invalid character in word '{}'".format(word))

        word = word.encode(encoding="ascii")
        result = cgaddag.gdg_add_word(self.gdg, word)
        if result == 1:
            raise ValueError("Invalid character in word '{}'".format(word))
        elif result == 2:
            raise MemoryError("Out of memory, GADDAG is in an undefined state")


def load(path):
    """
    Load a GADDAG from file.

    Args:
        path: path to saved GADDAG to be loaded.

    Returns:
        Loaded GADDAG.
    """
    gdg = GADDAG()
    gdg.load(path)

    return gdg

