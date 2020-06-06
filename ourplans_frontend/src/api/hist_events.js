import axios from "axios";

async function getEvents(date) {
  const res = await axios
    .get(
      `http://history.muffinlabs.com/date/${date.getMonth()}/${date.getDay()}`
    )
    .then((res) => console.log(res))
    .catch((err) => console.log(err));
}

export { getEvents };
