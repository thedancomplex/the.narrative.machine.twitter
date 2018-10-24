void goto_machine_zero()
{
  Serial.println("init");
  move_to_max(X_MIN_PIN, X_STEP_PIN, X_DIR_PIN, 0);
  move_to_max(Y_MIN_PIN, Y_STEP_PIN, Y_DIR_PIN, 0);
  Serial.println("ok");
}

void move_to_max(int limiter_pin, int stepper_pin, int stepper_dir_pin,int dir)
{
  /* Moves to the maximum possible position
  */
  while(can_step(limiter_pin, limiter_pin, 0, 1, dir)){
    do_step(stepper_pin, stepper_dir_pin, 0);
    delay(1);
  }
  // slowly back unitl pin is released
  while(!can_step(limiter_pin, limiter_pin, 0, 1, dir)){
    do_step(stepper_pin, stepper_dir_pin, 1);
    delay(10);
  }
}

bool can_step(byte min_pin, byte max_pin, long current, long target, byte direction)
{
  //stop us if we're on target
  if (target == current)
    return false;
  //stop us if we're at home and still going 
  else if (read_switch(min_pin) && !direction)
    return false;
  //stop us if we're at max and still going
  else if (read_switch(max_pin) && direction)
    return false;

  //default to being able to step
  return true;
}

void do_step(byte pinA, byte pinB, byte dir)
{
        switch (dir << 2 | digitalRead(pinA) << 1 | digitalRead(pinB)) {
            case 0: /* 0 00 -> 10 */
            case 5: /* 1 01 -> 11 */
                digitalWrite(pinA, HIGH);
                break;
            case 1: /* 0 01 -> 00 */
            case 7: /* 1 11 -> 10 */
                digitalWrite(pinB, LOW);
                break;
            case 2: /* 0 10 -> 11 */
            case 4: /* 1 00 -> 01 */   
                digitalWrite(pinB, HIGH);
                break;
            case 3: /* 0 11 -> 01 */
            case 6: /* 1 10 -> 00 */
                digitalWrite(pinA, LOW);
                break;
        }
        //dan
  delayMicroseconds(1);
}


bool read_switch(byte pin)
{
  //dual read as crude debounce
  
  if ( SENSORS_INVERTING )
    return !digitalRead(pin) && !digitalRead(pin);
  else
    return digitalRead(pin) && digitalRead(pin);
}











