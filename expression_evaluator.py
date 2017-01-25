'''
    Evaluator class evaluates arithemetic logical expression.
    This class is initialized with input json data.
    Each expression is an array with [operator, operand, comparison_value] and
    operand and comparison value could be Absolute value or an expression too

    INPUT: {"user": {"address": {"city": "mumbai", "zipcode": "122212"}}}
    expression: ['EQ', 'user.address.city', 'mumbai']
    return: True

    Run commond: python expression_evaluator.py
'''


class Evaluator:

    def __init__(self, json_obj):
        self.json_obj = json_obj

    '''
        This is operator mapping for input value to its
        python specific operators
    '''
    operators_mapping = {
        'EQ': '==',
        'GT': '>',
        'LT': '<',
        'IN': 'in',
        'AND': 'and',
        'OR': 'or',
        'NOT': 'not'
    }

    def expression_eval(self, exp):
        '''
            If operand or comparison_value are expression,
            then by recurrsion they are evaluated first
            other wise they are evaluated on set operator
        '''
        if not exp:
            return False

        operator = exp[0]
        if isinstance(exp[1], list):
            operand = self.expression_eval(exp[1])
        else:
            operand = exp[1]

        if isinstance(exp[2], list):
            comparison_value = self.expression_eval(exp[2])
        else:
            comparison_value = exp[2]

        return self.evaluate_operator(operator, operand, comparison_value)

    def is_operator(self, operator):
        '''
            Checks if given operator is a valid operator
        '''
        return operator in self.operators_mapping.keys()

    def evaluate_operator(self, operator, operand, comparison_value):
        '''
            This methods returns the evaluated value for given parameters.
            Checks if given operand is absolute value then it returns the
            value itself otherwise it evaluates it value first.
        '''
        if not isinstance(operand, str):
            return operand

        result = self.get_dot_notion_value(operand)
        operator = self.operators_mapping.get(operator)
        eval_string = '"{a}"{b}"{c}"'.format(a=result,
                                             b=operator,
                                             c=comparison_value)
        return eval(eval_string) or operand

    def get_dot_notion_value(self, dot_string):
        '''
            This method gets value of dot string input
            from input json object
        '''
        keys = dot_string.split('.')
        result = self.json_obj
        for key in keys:
            if not result:
                return None
            result = result.get(key, None)

        return result


if __name__ == "__main__":
    '''
        Sample input string
    '''
    inp = {"widget": {
        "debug": "on",
        "window": {
            "title": "Sample Konfabulator Widget",
            "name": "main_window",
            "width": 500,
            "height": 500
        },
        "image": {
            "src": "Images/Sun.png",
            "name": "sun1",
            "hOffset": 250,
            "vOffset": 250,
            "alignment": "center"
        },
        "text": {
            "data": "Click Here",
            "size": 36,
            "style": "bold",
            "name": "text1",
            "hOffset": 250,
            "vOffset": 100,
            "alignment": "center",
            "onMouseUp": "sun1.opacity = (sun1.opacity / 100) * 90;"
        }
    }}
    evaluator = Evaluator(inp)
    '''
        Sample expression
    '''
    exp1 = ["EQ", "widget.window.name", "main_window"]
    exp2 = ["GT", "widget.window.width", 200]
    exp3 = ["GT", "widget.image.hOffset", 300]
    exp4 = ["AND", ["GT", "widget.image.hOffset", 300],
            ["GT", "widget.window.width", 200]]

    '''
        Output for each expression
    '''
    print exp1, evaluator.expression_eval(exp1)
    print exp2, evaluator.expression_eval(exp2)
    print exp3, evaluator.expression_eval(exp3)
    print exp4, evaluator.expression_eval(exp4)
