from xlsxwriter.workbook import Workbook
from django.http import HttpResponse


def my_view(request):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = "attachment; filename=Expences01.xlsx"
    book = Workbook(response, {'in_memory': True})
    sheet = book.add_worksheet('test')
    sheet.write(0, 0, 'Hello, world!')
    book.close()

    return response
    # workbook = xlsxwriter.Workbook('Expences01.xlsx')
    # worksheet = workbook.add_worksheet()
    #
    # expenses = (
    #     ['Bakay', 2],
    #     ['Anna', 4],
    #     ['Tariel', 6],
    #     ['Islam', 2],
    # )
    #
    # row = 0
    # col = 0
    #
    # for item, cost in expenses:
    #     worksheet.write(row, col, item)
    #     worksheet.write(row, col + 1, cost)
    #     row += 1
    #
    # count = 'B' + str(row)
    # worksheet.write(row, 0, 'Total')
    # worksheet.write(row, 1, '=SUM(B1:%s)' % count)
    #
    # workbook.close()


