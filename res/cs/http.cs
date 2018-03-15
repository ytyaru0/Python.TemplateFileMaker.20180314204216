namespace ConsoleApplication
{
    public class Program
    {
        // https://docs.microsoft.com/ja-jp/aspnet/web-api/overview/advanced/calling-a-web-api-from-a-net-client#create-the-console-application
        /*
            コンパイル   $ mcs /reference:System.Net.Http.dll http.cs 
            実行         $ ./http.exe
        */
        public static void Main()
        {
            Console.WriteLine("Start.");
            GetGoogle().GetAwaiter().GetResult();
            Console.WriteLine("End.");
        }

        public static async Task GetGoogle() 
        {
            using(var client = new HttpClient())
            {
                var result = await client.GetAsync("https://www.google.co.jp");
                Console.WriteLine(result.StatusCode);
            }
        }
    }
}
