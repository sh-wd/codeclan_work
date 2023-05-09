import Counter from '../components/Counter';
import React from 'react';
import {render, fireEvent, waitFor} from "@testing-library/react";


describe("Counter", () => {

  let container

  beforeEach(() => {
    container = render(<Counter/>)
  });

  it('should start the counter at zero', () => {
    const counter = container.getByTestId("counter");
    expect(counter.textContent).toEqual("0");
  });

  it("should increment counter on click", () => {
    const upButton = container.getByTestId("button-up");
    fireEvent.click(upButton);
    const counter = container.getByTestId("counter");
    expect(counter.textContent).toEqual("1");
  });

  it("should decrement counter on click", () => {
    const downButton = container.getByTestId("button-down");
    fireEvent.click(downButton);
    const counter = container.getByTestId("counter");
    expect(counter.textContent).toEqual("-1");
  });

});