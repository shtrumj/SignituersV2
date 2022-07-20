// async function cyfetch() {
//     const url = 'https://cybernet.cyber.gov.il/api/rest/getIndicators?fromDate=2010-10-10_00%3A00%3A00'
//     const response = await fetch (url,
//         {
//             method: 'GET',
//             headers: {
//                 'CN-USER-NAME' : 'soc_trot',
//                 'X-API-KEY' : '1E804161881901AB',
//                 'Authorization' : 'Basic Og=="'
//             }
//         }
//         ).then(response => {
//             console.log(response)
//         }
//     );
//     const data = await response.json();
//     console.log(data)
async function cyfetch() {
    var myHeaders = new Headers();
    myHeaders.append("Access-Control-Allow-Origin", "http://127.0.0.1:4444");
    myHeaders.append("CN-USER-NAME", "soc_trot");
    myHeaders.append("Content-Type", "application/json")
    myHeaders.append("X-API-KEY", "1E804161881901AB");
    myHeaders.append("Authorization", "Basic Og==");
    myHeaders.append("Cookie", "LastMRH_Session=b8c05467; MRHSession=1da3978fd1960afc055af4c9b8c05467");

    var requestOptions = {
        method: 'GET',
        mode: 'cors',
        headers: myHeaders,
        redirect: 'follow'
    };

    fetch("https://cybernet.cyber.gov.il/api/rest/getIndicators?fromDate=2010-10-10_00%3A00%3A00", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
}


// /usr/bin/curl -vv --request GET \
//   --url 'https://cybernet.cyber.gov.il/api/rest/getIndicators?fromDate=2010-10-10_00%3A00%3A00' \
//   --header 'CN-USER-NAME: soc_trot' \
//   --header 'X-API-KEY: 1E804161881901AB' \
//   --cookie 'LastMRH_Session=ca096017; MRHSession=7ba73d73eee4f2d328cceeb0ca096017'\
//   -o  output.txt
