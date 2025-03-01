class Solution:
    def simplifyPath(self, path: str) -> str:
        path_entries = path.split('/')
        simple_path = []

        curr = ""
        for i in range(1, len(path_entries)):
            el = path_entries[i]
            if el == '..':
                if len(simple_path) > 0:
                    simple_path.pop()
            elif el == '.' or el == '':
                continue
            else:
                simple_path.append(el)

        return '/' + '/'.join(simple_path)