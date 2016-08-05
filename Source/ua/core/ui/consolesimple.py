class ConsoleSimple:
            
    def clear_line(self):
        '''Doesn't do anything here'''
        pass
    
    def clear_screen(self):
        '''Doesn't do anything here'''
        pass
    
    def newline(self):
        print ('')
    
    def print(self, text):
        ''' Can't do this so doesn't try.
        '''
        self.print_line(text)
        
    def print_line(self, text = ""):
        ''' Print and move to new line.
        '''
        print (text)
        
    def read_line(self):
        
        text = input()
        self._last_line_le
        
        return text
    
    def read_key(self):

        value = input()
        
        if not value:
            value = chr(13)
             
        elif value == 'del':
            value = chr(127)
            
        elif value == 'ctlc':
            value = chr(3)
            
        elif len(value) > 1:
            value = value[1]
        
        return value
    
    def read_key_value(self):

        return ord(self.read_key())

