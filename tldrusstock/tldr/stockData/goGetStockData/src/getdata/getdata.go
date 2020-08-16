package getdata

import (
	"github.com/piquette/finance-go/quote"
	"fmt"
	"strings"
	"sync"
	// "encoding/json"
)

type StockData struct {
	Name string
	Ticker string 
	Price float64 
	Change float64 
	Error bool 
}

func (data StockData) String() string {
	if data.Error {
		return "{'name' : '', 'ticker' : '', 'price' : 0, 'change' : 0, 'error' : true}"
	} else {
		return fmt.Sprintf("{'name' : '%v', 'ticker' : '%v', 'price' : %.2f, 'change' : %.2f, 'error' : false}",
												data.Name, data.Ticker, data.Price, data.Change)
	}
}

func getOneQuote(t string) StockData {
	q, err := quote.Get(t)
	if err != nil {
		fmt.Println("quote.Get() error:", err)
	}

	// return this if quote is invalid
	d := StockData{"", "", 0.0, 0.0, true}

	if q != nil {
		// name := 
		// ticker := 
		// price := fmt.Sprintf("%.2f", q.RegularMarketPrice)
		// change := fmt.Sprintf("%.2f", q.RegularMarketChangePercent)
		d = StockData{q.ShortName, q.Symbol, q.RegularMarketPrice, q.RegularMarketChangePercent, false}
	}

	return d

	// res, err := json.Marshal(d)

	// if err != nil {
	// 	fmt.Println("json.Marshal() error:", err)
	// }

	// return res
}

func GetQuote(l string) string {
	// clean the string
	list := strings.Split(l[2:len(l)-2], "', '")
	res := make([]string, len(list))

	// use wait group to synchronize
	wg := sync.WaitGroup{}
	wg.Add(len(list))

	for i, v := range list {
		go func (idx int, t string) {
			defer wg.Done()
			res[idx] = getOneQuote(t).String()
		} (i, v)
	}

	wg.Wait()



	return "[" + strings.Join(res, ", ") + "]"
}