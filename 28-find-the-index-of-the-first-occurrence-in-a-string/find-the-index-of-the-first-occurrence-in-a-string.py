class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack) or len(needle) == 0: return -1
        if needle == haystack: return 0

        for l in range(len(haystack)):
            if haystack[l:l+len(needle)] == needle:
                return l

            # if haystack[l] == needle[0]:
            #     idx_haystack = l
            #     idx_needle = 0

            #     while idx_haystack < len(haystack) and idx_needle < len(needle) and haystack[idx_haystack] == needle[idx_needle]:
            #         idx_haystack += 1
            #         idx_needle += 1
                
            #     if idx_needle == len(needle):
            #         return l
            

        return -1

        '''
        "sadbutsad"
            h

        "sad"
            n


        '''