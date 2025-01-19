class Solution(object):
    def simplifyPath(self, path):
        folders = path.split("/")
        folders = list(map(self.parse, folders))
        folders = filter(self.removeEmpty, folders)
        
        res = ""
        i = len(folders) - 1
        while i >= 0:
            if folders[i] == ".":
                i -= 1
            elif folders[i] == "..":
                i -= 2
            else:
                res = "/" + folders[i] + res
                i -= 1
        
        if not res: return "/"
        return res


    def removeEmpty(self, folder):
        return len(folder) > 0
        
        
    def parse(self, folder):
        return folder.replace("/", "")