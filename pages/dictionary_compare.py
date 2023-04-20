
class DictionaryCompare:

    def compare_dicts(dict1, dict2):
        for key in dict1.keys():
            if key not in dict2:
                return False
            if dict1[key] != dict2[key]:
                return False
        for key in dict2.keys():
            if key not in dict1:
                return False
        return True
