def largest(min_factor, max_factor):
    '''
    Returns the largest palindrome product and its factors

    :param min_factor:
    :param max_factor:
    :return:
    '''

    return main_func(min_factor, max_factor, False)


def smallest(min_factor, max_factor):
    '''
    Returns the smallest palindrome product and its factors

    :param min_factor:
    :param max_factor:
    :return:
    '''

    return main_func(min_factor, max_factor, True)


def main_func(min_factor, max_factor, is_smallest):

    products = get_products(min_factor, max_factor, is_smallest)

    if not products:
        return None, []

    if is_smallest:
        palindrome = min(products.keys())
    else:
        palindrome = max(products.keys())

    factors = products[palindrome]

    return palindrome, factors


def get_products(min_factor, max_factor, is_smallest):
    '''
    Generate a list of factors between specified range

    :param min_factor:
    :param max_factor:
    :param is_smallest:
    :return:
    '''

    # Raise an error in case min > max
    if min_factor > max_factor:
        raise ValueError(".+")

    if min_factor == max_factor:
        return None

    nums = dict()
    min_f = min_factor
    while min_factor <= max_factor:
        m = min_f
        while m <= max_factor:
            n = min_factor * m
            if is_palindrome(n):
                if not nums:
                    nums[n] = [[min_factor, m]]
                else:
                    if is_smallest:
                        if n < min(nums.keys()):
                            nums[n] = [[min_factor, m]]
                        elif n == min(nums.keys()):
                            if [min_factor, m] not in nums[n]:
                                nums[n].append([min_factor, m])
                        else:
                            return nums
                    else:
                        if n > max(nums.keys()):
                            nums[n] = [[min_factor, m]]
                        elif n == max(nums.keys()):
                            if [min_factor, m] not in nums[n]:
                                nums[n].append([min_factor, m])

            m += 1
        min_factor += 1

    return nums


def is_palindrome(number):
    '''
    Reverse string and compare to itself.
    Returns True uin case number is palindrome, false otherwise.
    :param number:
    :return:
    '''

    return str(number) == str(number)[::-1]

