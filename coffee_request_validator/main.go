package main

import (
	"fmt"
	"strconv"
)

func main() {
	var frameLength int
	fmt.Scan(&frameLength)
	//frameLength = 611
	var frame string
	fmt.Scan(&frame)
	//frame = "0D2F1A99257FEE9DE46F3A91E0825D8BD9335A5D703A3FD418A61B62584786724682A71D5772F73F14140D69C24D807C9ED68B7C1FFCFD6A57EBE7236C5DF4525B58862B2088909B54D983C3529C05DA173E6B9B4C06C3C7F720039EBA21B1F666F8CACFF382C9CC218209BE5519910C0BAB124D39AD2E88D89F8024E4336452FFC33A792F976D07B3592D95DB0084A86CF956AAC9F8AA457B4683F19835AE464091D9B564CF46BF533489E73D0220999B152258B7ACC68493FFA65A5423D33D0E5D7F3D1A9ECF556F767328C2B7AB3C94F2D5431C54EBE8477C667C3BF0973701ABFE31BD63314B4ACD8CABE8AEE7909064819D8649B9E0222B1780A05BF26A8E74370D44EE8DB94E82F8B438B5707F421FB2C4F2B2F7D6124D51077E8B43F585F26AE7254F856F82D80E8BC8E344E9F94"

	var orderSize int64
	var header string
	var frameSize string
	var orderData string
	var checksum string
	orders := make(map[string]int)

	if frameLength < 13 {
		fmt.Println("403 Forbidden")
		return
	}

	frameSize = frame[8:11]

	orderSize, _ = strconv.ParseInt(frameSize, 16, 64)
	if orderSize != (int64(frameLength) - 12) {
		fmt.Println("403 Forbidden")
		return
	}

	header = frame[:8]
	if header != "DECAFBAD" {
		fmt.Println("403 Forbidden")
		return
	}

	orderData = frame[11 : frameLength-1]

	checksum = frame[frameLength-1:]
	_ = checksum

	var tot int64
	for _, val := range frame {
		hex, _ := strconv.ParseInt(string(val), 16, 64)
		tot += hex
	}

	if tot%16 != 0 {
		fmt.Println("403 Forbidden")
	} else {

		var ord []string

		for i := 0; i < int(orderSize); i++ {
			if orders[string(rune(orderData[i]))] == 0 {
				orders[string(rune(orderData[i]))] = 1
				ord = append(ord, string(rune(orderData[i])))
			} else {
				orders[string(rune(orderData[i]))]++
			}
		}

		for _, i := range ord {
			fmt.Println(orders[i], i)
		}
	}
}
