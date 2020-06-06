import React from "react";
import { DateContext } from "../context/Context";
import { getEvents } from "../api/hist_events";
export default () => {
  const { date } = React.useContext(DateContext);
  const event_date = new Date(date);
  getEvents(event_date).then((res) => console.log(res));
  return (
    <div>
      <h3>Your Date: {date}</h3>
      <p>{event_date.getDay()}</p>
    </div>
  );
};
