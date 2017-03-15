import pdb

class CustomerIter:
    def __init__(self, indices, max):
        self.current = 0
        self.indices = indices
        self.count = 0
        self.high = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > len(self.indices):
            return StopIteration, StopIteration
        elif self.count == len(self.indices):
            self.count += 1
            low = self.current
            return low, self.high
        else:
            low = self.current
            self.current = self.indices[self.count]
            self.count += 1
            return low, self.current

class FilePathTokenizer:
    def __init__(self):
        self.tokenized = {}

    def tokenize_file_paths(self, file_paths):
        # iterate over the paths
        for path in file_paths:

            # find character indices of backslash
            directory_indices = []
            for i in range(len(path)):
                if path[i] == "\\":
                    directory_indices.append(i)

            # splice path into tokens in between backslash indices
            tokens = []
            for low, high in CustomerIter(directory_indices, len(path)):
                if low is StopIteration:
                    break
                if low != 0:
                    tokens.append(path[low+1:high])
                else:
                    tokens.append(path[low:high])

            # find the file extension position -- if it exists
            extension_index = None
            for i in range(len(tokens[len(tokens)-1])):
                if tokens[len(tokens)-1][i] == ".":
                    extension_index = i
            if extension_index:
                tokens.append(path[directory_indices[len(directory_indices)-1]+1:directory_indices[len(directory_indices)-1]+1+extension_index])
                tokens.append(path[directory_indices[len(directory_indices)-1]+extension_index+1:len(path)])

            # find the path (excluding the drive name) to the file (excluding the file name)
            if extension_index:
                tokens.append(path[directory_indices[0]+1:directory_indices[len(directory_indices)-1]])
            else:
                tokens.append(path[directory_indices[0]+1:len(path)])

            # add new path to dictionary
            self.tokenized[path] = tokens

        return self.tokenized

    def tokenize_fd(self, fd):
        # TODO:
            # open and read paths from files
            # check for errors
            # create list of paths
            # call tokenize_file_paths
        pdb.set_trace()
        return self.tokenized

    def tokenize_file_path(file_path):
        return tokenize_file_paths(file_path)

    def print_tokens(self):
        for path in self.tokenized:
            # print(self.tokenized[path])
            print("[{0}]".format(", ".join(self.tokenized[path])))
            # print(',  '.join(self.tokenized[path]))
