class InvoicesScript:
    invoice_numbers = [
        100, 120, 130, 35, 79,
        10, 145, 105, 110, 115
    ]

    invoice_totals = [
        350.45, 45.00, 250.37, 15.32, 255.19,
        3.75, 8.79, 127.10, 399.00, 78.66
    ]

    running_sum_array = []
    sum = 0

    for inv_total in invoice_totals:
        sum += inv_total
        running_sum_array .append(round(sum, 2))

    print("Original Array Invoice Numbers = {}".format(invoice_numbers))
    print("Original Array Invoice Totals = {}".format(invoice_totals))
    print("Array Running Sum of Invoices Totals = {}".format(running_sum_array))

    def sort_invoices_ascending(self):
        invoices_map = {}

        for inv_num, inv_total in zip(self.invoice_numbers, self.invoice_totals):
            invoices_map[inv_num] = inv_total

        # sort invoices_map
        sorted_invoices_map = sorted(invoices_map.items(), key=lambda kv: kv[1])

        asc_inv_numbers = []
        asc_inv_totals = []

        for inv_num, inv_total in sorted_invoices_map:
            asc_inv_numbers.append(inv_num)
            asc_inv_totals.append(inv_total)

        print()
        print("Ascending Array Invoice Numbers = {}".format(asc_inv_numbers))
        print("Ascending Array Invoice Totals = {}".format(asc_inv_totals))


if __name__ == "__main__":
    InvoicesScript().sort_invoices_ascending()
