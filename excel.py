
# Import openpyxl 
import openpyxl 
  

  
# Print the list of names 


def GetPhoneList(file,ColumnName):
    # Open the spreadsheet 
    workbook = openpyxl.load_workbook(file) 
    
    # Get the first sheet 
    sheet = workbook.worksheets[0] 
    
    # Create a list to store the values 
    names = [] 
    
    # Iterate through columns 
    for column in sheet.iter_cols(): 
        # Get the value of the first cell in the 
        # column (the cell with the column name) 
        column_name = column[0].value 
        # Check if the column is the "Name" column 
        if column_name == ColumnName: 
            # Iterate over the cells in the column 
            for cell in column:
                if cell.value == column_name or cell.value == None:
                    continue
                # Add the value of the cell to the list 
                names.append(cell.value) 

    return names
