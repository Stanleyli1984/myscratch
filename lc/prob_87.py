# class Solution:
#     # @param {string} s1
#     # @param {string} s2
#     # @return {boolean}
#     def isScramble(self, s1, s2):
#         self.s1 = s1
#         self.s2 = s2
#         if self.count_dict(s1, (0, len(s1))) == self.count_dict(s2, (0, len(s2))):
#             return self.recurs((0, len(s1)), (0, len(s2)))
#         else:
#             return False
#
#     def count_dict(self, string, s1_pos):
#         t1 = {}
#         for i in xrange(s1_pos[0], s1_pos[1]):
#             if string[i] in t1:
#                 t1[string[i]] += 1
#             else:
#                 t1[string[i]] = 1
#         return t1
#
#     def recurs(self, s1_poses, s2_poses):
#         if s1_poses[1] - s1_poses[0] <= 3:
#             return True
#         dict_1 = self.count_dict(self.s1, (s1_poses[0], (s1_poses[0] + s1_poses[1])/2))
#         dict_2 = self.count_dict(self.s2, (s2_poses[0], (s2_poses[0] + s2_poses[1])/2))
#         dict_3 = self.count_dict(self.s2, ((s2_poses[0] + s2_poses[1] + 1)/2, s2_poses[1]))
#
#         if dict_1 == dict_2:
#             result = self.recurs((s1_poses[0], (s1_poses[0] + s1_poses[1])/2), (s2_poses[0], (s2_poses[0] + s2_poses[1])/2)) and \
#                 self.recurs(((s1_poses[0] + s1_poses[1])/2, s1_poses[1]), ((s2_poses[0] + s2_poses[1])/2, s2_poses[1]))
#             if result:
#                 return True
#             elif dict_1 == dict_3:
#                 return self.recurs((s1_poses[0], (s1_poses[0] + s1_poses[1])/2), ((s2_poses[0] + s2_poses[1] + 1)/2, s2_poses[1])) and \
#                     self.recurs(((s1_poses[0] + s1_poses[1])/2, s1_poses[1]), (s2_poses[0], (s2_poses[0] + s2_poses[1] + 1)/2))
#             else:
#                 return False
#         elif dict_1 == dict_3:
#             result = self.recurs((s1_poses[0], (s1_poses[0] + s1_poses[1])/2), ((s2_poses[0] + s2_poses[1] + 1)/2, s2_poses[1])) and \
#                 self.recurs(((s1_poses[0] + s1_poses[1])/2, s1_poses[1]), (s2_poses[0], (s2_poses[0] + s2_poses[1] + 1)/2))
#             if result:
#                 return True
#             elif dict_1 == dict_2:
#                 return self.recurs((s1_poses[0], (s1_poses[0] + s1_poses[1])/2), (s2_poses[0], (s2_poses[0] + s2_poses[1])/2)) and \
#                     self.recurs(((s1_poses[0] + s1_poses[1])/2, s1_poses[1]), ((s2_poses[0] + s2_poses[1])/2, s2_poses[1]))
#             else:
#                 return False
#         return False
#
# print Solution().isScramble("abab", "aabb")

class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
        if self.count_dict(s1, (0, len(s1))) == self.count_dict(s2, (0, len(s2))):
            return self.recurs((0, len(s1)), (0, len(s2)))
        else:
            return False

    def count_dict(self, string, s1_pos):
        t1 = {}
        for i in xrange(s1_pos[0], s1_pos[1]):
            if string[i] in t1:
                t1[string[i]] += 1
            else:
                t1[string[i]] = 1
        return t1

    def recurs(self, s1_poses, s2_poses):
        if s1_poses[1] - s1_poses[0] <= 3:
            return True
        dict_1s = [None]
        for i in xrange(1, s1_poses[1] - s1_poses[0]):
            dict_1s.append(self.count_dict(self.s1, (s1_poses[0], s1_poses[0] + i)))
            dict_2 = self.count_dict(self.s2, (s2_poses[0], s2_poses[0] + i))
            if dict_1s[i] == dict_2:
                if self.recurs((s1_poses[0], s1_poses[0] + i), (s2_poses[0], s2_poses[0] + i)) and \
                    self.recurs((s1_poses[0] + i, s1_poses[1]), (s2_poses[0] + i, s2_poses[1])):
                    return True

        for i in xrange(1, s1_poses[1] - s1_poses[0]):
            dict_2 = self.count_dict(self.s2, (s2_poses[1]-i, s2_poses[1]))
            if dict_1s[i] == dict_2:
                if self.recurs((s1_poses[0], s1_poses[0] + i), (s2_poses[1]-i, s2_poses[1])) and \
                    self.recurs((s1_poses[0] + i, s1_poses[1]), (s2_poses[0], s2_poses[1]-i)):
                    return True
        return False

print Solution().isScramble("rgeat", "great")
