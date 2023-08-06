## EXAL - Excel Abstraction Layer

Abstraction layer for multible Excel wrapper.

#### Supportet Wrappers:
- win32com
- xlwings
- comtype
- openpyxl

#### Sample usage:

```Python
import exal
import exal.helper as helper

wb = ex_driver.open_workbook_from_file("tests/testbook.xlsx")

print [sh.name for sh in wb.sheets]

sh = wb.get_sheet("Sheet1")

print sh.range((1,1), (2,2)).value
print sh.range((1,1), (2,2)).formula

sh.cell((3,3)).formula = "=" + helper.pos2address(1,1)
print sh.cell((3,3)).value
wb.save_as("test_out.xlsx")
wb.close()
```

## Authors

* **Kevin Gliewe** - [KevinGliewe](https://github.com/KevinGliewe)

## License

This project is licensed under the LGPLv3 License - see the [LICENSE.md](LICENSE.md) file for details