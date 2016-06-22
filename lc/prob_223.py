class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        total = (C-A) * (D-B) + (H-F) * (G-E)
        lengths = [None] * 2
        for i, group in enumerate([(A,C,E,G), (B,D,F,H)]):
            lengths[i] = min(group[1], group[3]) - max(group[0], group[2])
            if lengths[i] <= 0:
                return total
            #if group[2] <= group[0] and group[1] <= group[3]:
            #    lengths[i] = group[1] - group[0]
            #elif group[0] <= group[2] and group[3] <= group[1]:
            #    lengths[i] = group[3] - group[2]
            #elif group[0] <= group[2] and group[1] <= group[3]:
            #    lengths[i] = group[1] - group[2]

        return total - lengths[0] * lengths[1]