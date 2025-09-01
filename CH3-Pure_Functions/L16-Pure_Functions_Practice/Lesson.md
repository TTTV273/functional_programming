# Pure Functions Practice

Datetimes are infamously a [pain in the neck](https://gist.github.com/timvisee/fcda9bbdff88d45cc9061606b4b923ca) for programming. The least of the list of problems are the order of the year, month and day of a calendar date. Some countries use day-month-year format, others use year-month-day. Some [insane countries](https://iso.mit.edu/americanisms/date-format-in-the-united-states/) use month-day-year because they want everyone else to be miserable.

## Assignment

Fix the `sort_dates` function. It takes as input a list of dates in `"MONTH-DAY-YEAR"` format and returns a list of the dates sorted in ascending order.

# Tips

The built-in [`sorted`](https://docs.python.org/3/library/functions.html#sorted) function might work better here than the `.sort()` list method. Create a function to transform the dates to make them easier to compare with the `sorted` function.

Pay attention to the expected date order. Is it ordered by day, month, or year?

The `sorted` function accepts a second optional parameter. This parameter is a function that will be called on each iteration.
