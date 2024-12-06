class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        visited = ""
        for char in s:
            if char in '({[':
                visited += char
            else:
                if not visited or \
                        (char == ')' and visited[-1] != '(') or \
                        (char == '}' and visited[-1] != '{') or \
                        (char == ']' and visited[-1] != '['):
                    return False
                visited = visited[:-1]
        return not visited
