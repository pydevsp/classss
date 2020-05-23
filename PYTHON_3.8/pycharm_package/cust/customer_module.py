class Customer:
    def __init__(self,cid,cname,caddr):
        self.cid = cid
        self.cname = cname
        self.caddr = caddr
    def getCustomerDetails(self):
        print("Customer Details")
        print("------------------------")
        print("Customer Id :",self.cid)
        print("Customer Name :",self.cname)
        print("Customer Address :",self.caddr)

