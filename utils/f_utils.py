def standard_object_type(df, columns):
    for col in columns:
        if(df[col].dtype != 'object'):
            df[col] = df[col].astype('object')

def type_conversion(df, columns):
    for col in columns:
        if col in df:
            df[col] = df[col].fillna(-1).astype('float32')

def type_conversion_64(df, columns):
    for col in columns:
        if col in df:
            df[col] = df[col].fillna(-1).astype('float64')
            
def column_factorize(df, columns):
    for col in columns:
        if col in df:
            df[col], factorize_map = df[col].factorize()
            df[col] = df[col].fillna(-1).astype('float32')

def column_factorize_64(df, columns):
    for col in columns:
        if col in df:
            df[col], factorize_map = df[col].factorize()
            df[col] = df[col].fillna(-1).astype('float64')

def clean_format_strings(df, columns):
    for col in columns:
        if col in df:
            df[col] = df[col].str.replace('%', '').fillna('-1').astype('float32')

def clean_format_strings_64(df, columns):
    for col in columns:
        if col in df:
            df[col] = df[col].str.replace('%', '').fillna('-1').astype('float64')

def clean_format_price(df, columns):
    for col in columns:
        if col in df:
            df[col] = df[col].str.replace(['$', ','], '').astype('float32')

def clean_format_price_64(df, columns):
    for col in columns:
        if col in df:
            df[col] = df[col].str.replace(['$', ','], '').astype('float64')

def clean_format_price_cpu(df, columns):
    for col in columns:
        if col in df:
            df[col] = df[col].fillna('-1').str.replace('$', '').str.replace(',', '').astype('float32')

def clean_format_price_64_cpu(df, columns):
    for col in columns:
        if col in df:
            df[col] = df[col].fillna('-1').str.replace('$', '').str.replace(',', '').astype('float64')
