def no_teen_sum(a, b, c):
    def fix_teen(n):
        if n in [13, 14, 17, 18, 19]:
            return 0
        return n

    return fix_teen(a) + fix_teen(b) + fix_teen(c)
