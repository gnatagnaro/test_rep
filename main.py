# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# s = '3' * 300 + '2' * 200
# while '33' in s or '22' in s:
#     if '33' in s:
#         s = s.replace('33', '2', 1)
#     else:
#         s = s.replace('22', '3', 1)
#
# print(s)

s = '1' * 63
while '111' in s:
    if '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '11', 1)

print(s)