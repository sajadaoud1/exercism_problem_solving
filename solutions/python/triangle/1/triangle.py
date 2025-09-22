def equilateral(sides):
    len1 = sides[0]
    len2 = sides[1]
    len3 = sides[2]
    if len1 == 0 or len2 == 0 or len3 ==0:
        return False
    elif sides[0] == sides[1]== sides[2]:
        return True
    else:
        return False


def isosceles(sides):
    len1 = sides[0]
    len2 = sides[1]
    len3 = sides[2]
    if len1 == len2 or len1 == len3 or len2 == len3:
        if len1 == len2:
            if len1 + len2 < len3:
                return False
        if len1 == len3:
            if len1 + len3 < len2:
                return False
        if len2 == len3:
            if len2 + len3 < len1:
                return False
            return True
        else:
            return True
    else:
        return False


def scalene(sides):
    len1 = sides[0]
    len2 = sides[1]
    len3 = sides[2]
    if len1 != len2 and len1 != len3 and len2 != len3:
        if len1 + len2 < len3:
            return False
        if len1+ len3 < len2:
            return False
        if len2 + len3 < len1:
            return False
        return True
    else:
        return False
