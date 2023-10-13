// Задача: Написать программу, которая из имеющегося массива строк 
// формирует новый массив из строк, длина которых меньше, либо равна 3 символам. 
// Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма. 
// При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.
// Примеры:
// [“Hello”, “2”, “world”, “:-)”] → [“2”, “:-)”]
// [“1234”, “1567”, “-2”, “computer science”] → [“-2”]
// [“Russia”, “Denmark”, “Kazan”] → []

//Выводим запрос на ввод количества элементов массива
Console.Write("Введите количество строк в массиве: ");
string[] stringArray = new string[Convert.ToInt32(Console.ReadLine())];
Console.WriteLine();
FillArray(stringArray);
Console.WriteLine();
PrintArray(StrLengthThree(stringArray));

//Метод ввода массива пользователем
string[] FillArray(string[] arrFill)
{
    for (int i = 0; i < arrFill.Length; i++)
    {
        Console.Write($"Введите {i + 1} строку массива: ");
        arrFill[i] = Console.ReadLine();
    }
    return arrFill;
}

//Метод вывода массива на печать
void PrintArray(string[] arrPrint)
{
    Console.Write("[");
    for (int i = 0; i < arrPrint.Length; i++)
    {
        Console.Write($"\"{arrPrint[i]}\"");
        if (i != arrPrint.Length - 1)
        {
            Console.Write(", ");
        }
    }
    Console.Write("]");
}

//Метод создания массива из введенного пользователем, с длиной строк меньше или равно 3
string[] StrLengthThree(string[] arrCheck)
{
    int count = 0;
    for (int i = 0; i < arrCheck.Length; i++)
    {
        if (arrCheck[i].Length <= 3)
        {
            count++;
        }
    }
    string[] array = new string[count];
    int index = 0;
    for (int i = 0; i < arrCheck.Length; i++)
    {
        if (arrCheck[i].Length <= 3)
        {
            array[index] = arrCheck[i];
            index++;
        }
    }
    return array;
}