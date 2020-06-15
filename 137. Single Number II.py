class Solutions(object):
    def singleNumber(self, nums):
        res = 0

        for i in range(32):
            bit_i_sum = 0

            for num in nums:
                bit_i_sum += (num >> i) & 1
            res += (bit_i_sum % 3) << i
        return res


if __name__ == '__main__':
    print(Solutions().singleNumber([0,1,0,1,0,1,99]))