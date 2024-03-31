#!/bin/bash

GETDATE=$(date "+%Y-%m-%d")

money=$(curl -X GET 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=trbi20dGwQLpPdFaGwOta4QA13A1NIDd&searchdate='$GETDATE'&data=AP01')

money_array=$(echo ${money:1:-1} | sed -e "s/},{/}?{/g")

(echo $money_array | tr '?' '\n') >>world_money.log