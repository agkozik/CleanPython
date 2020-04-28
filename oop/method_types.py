class MyClass:
    def method(self):
        return 'вызван метод экземпляра', self

    @classmethod
    def classmethod(cls):
         return 'вызван метод класса', cls

    @staticmethod
    def staticmethod():
         return 'вызван статический метод'


obj = MyClass()

print(obj.method())
print(MyClass.method(obj))


print(obj.classmethod())
print(MyClass.classmethod())


print(obj.staticmethod())
print(MyClass.staticmethod())