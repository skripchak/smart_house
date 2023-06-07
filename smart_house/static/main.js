let all_data = [];

const houses = document.querySelectorAll('.house');

function average(data) {
    let sum = 0;
    data.forEach(el => {
        sum += el;
    });

    return Math.floor(sum / data.length);
}

async function monitor() {
    await fetch(`http://127.0.0.1:8000//monitor/`)
        .then(response => response.json())
        .then(data => {
            const consumption = document.querySelectorAll('.outlet .consumption');
            consumption.forEach((el, index) => {
                el.innerText = 'Consumption:' + data[index][data[index]['house']] + 'W';
                if (data[index][data[index]['house']] > 900) {
                    el.style.color = 'red';
                } else el.style.color = 'green';
            });

            data.forEach(el => {
                all_data.push(el);
            });

            for (const data of all_data) {
                // console.log(data[data.house]);
            }

            houses.forEach((house, index) => {
                let house_number = index + 1;
                const house_data = [];
                data.forEach(el => {
                    if (house_number === el.house) {
                        house_data.push(el[house_number]);
                    }
                });
                house.querySelectorAll('.average span').forEach(el => {
                    el.innerText = average(house_data) + 'W';
                    if (average(house_data) > 1100) {
                        el.style.color = 'red';
                    } else el.style.color = 'green';
                });
                house.querySelectorAll('.max span').forEach(el => el.innerText = Math.max(...house_data) + 'W');
                house.querySelectorAll('.min span').forEach(el => el.innerText = Math.min(...house_data) + 'W');
            });
        });

    await new Promise(r => setTimeout(r, 1000));
    await monitor();
}

monitor();