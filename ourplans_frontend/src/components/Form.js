import React from "react";
import { useForm } from "react-hook-form";
import { DateContext } from "../context/Context";

const Input = ({ value, onChange, name, id, type, register, required }) => (
  <>
    <label htmlFor={name}>{name} </label>
    <input
      ref={register({ required })}
      value={value}
      onChange={(event) => onChange({ value: event.target.value })}
      name={name}
      id={id}
      type={type}
    />
  </>
);

export default function Form() {
  const { register, handleSubmit, watch, errors } = useForm();
  const { date, setDate } = React.useContext(DateContext);
  const onSubmit = (data) => {
    console.log(data);    
  };
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <Input
        value={date}
        onChange={setDate}
        name="date"
        id="date"
        type="date"
        register={register}
      />
      {errors.date && <span>Please select a date</span>}
      <input type="submit" value="Submit" />
    </form>
  );
}
