from sqlalchemy import Column, Integer, Float, Date, Time, String, DateTime

from app.database.base import Base


class GarminDailySummary(Base):
    __tablename__ = "garmin_daily_summaries"

    day = Column(Date, primary_key=True, index=True)
    hr_avg = Column(Float)
    hr_min = Column(Float)
    hr_max = Column(Float)
    rhr_avg = Column(Float)
    rhr_min = Column(Float)
    rhr_max = Column(Float)
    inactive_hr_avg = Column(Float)
    inactive_hr_min = Column(Float)
    inactive_hr_max = Column(Float)
    weight_avg = Column(Float)
    weight_min = Column(Float)
    weight_max = Column(Float)
    intensity_time = Column(Time, nullable=False)
    moderate_activity_time = Column(Time, nullable=False)
    vigorous_activity_time = Column(Time, nullable=False)
    intensity_time_goal = Column(Time, nullable=False)
    steps = Column(Integer)
    steps_goal = Column(Integer)
    floors = Column(Float)
    floors_goal = Column(Float)
    sleep_avg = Column(Time, nullable=False)
    sleep_min = Column(Time, nullable=False)
    sleep_max = Column(Time, nullable=False)
    rem_sleep_avg = Column(Time, nullable=False)
    rem_sleep_min = Column(Time, nullable=False)
    rem_sleep_max = Column(Time, nullable=False)
    stress_avg = Column(Integer)
    # calories_avg = Column(Integer)
    # calories_bmr_avg = Column(Integer)
    # calories_active_avg = Column(Integer)
    # calories_goal = Column(Integer)
    # calories_consumed_avg = Column(Integer)
    activities = Column(Integer)
    activities_calories = Column(Integer)
    activities_distance = Column(Integer)
    # hydration_goal = Column(Integer)
    # hydration_avg = Column(Integer)
    # hydration_intake = Column(Integer)
    sweat_loss_avg = Column(Integer)
    sweat_loss = Column(Integer)
    spo2_avg = Column(Float)
    spo2_min = Column(Float)
    rr_waking_avg = Column(Float)
    rr_max = Column(Float)
    rr_min = Column(Float)
    bb_max = Column(Integer)
    bb_min = Column(Integer)

    def __repr__(self):
        return f"<GarminDailySummary(day='{self.day}', steps={self.steps}, hr_avg={self.hr_avg})>"


class GarminActivity(Base):
    __tablename__ = "garmin_activities"

    activity_id = Column(String, primary_key=True, index=True)
    name = Column(String)
    # description = Column(String)
    type = Column(String)
    # course_id = Column(Integer)
    laps = Column(Integer)
    sport = Column(String)
    sub_sport = Column(String)
    # device_serial_number = Column(Integer)
    self_eval_feel = Column(String)
    self_eval_effort = Column(String)
    training_load = Column(Float)
    training_effect = Column(Float)
    anaerobic_training_effect = Column(Float)
    start_time = Column(DateTime)
    stop_time = Column(DateTime)
    elapsed_time = Column(Time, nullable=False)
    moving_time = Column(Time, nullable=False)
    distance = Column(Float)
    cycles = Column(Float)
    avg_hr = Column(Integer)
    max_hr = Column(Integer)
    avg_rr = Column(Float)
    max_rr = Column(Float)
    calories = Column(Integer)
    avg_cadence = Column(Integer)
    max_cadence = Column(Integer)
    avg_speed = Column(Float)
    max_speed = Column(Float)
    ascent = Column(Float)
    descent = Column(Float)
    # max_temperature = Column(Float)
    # min_temperature = Column(Float)
    # avg_temperature = Column(Float)
    start_lat = Column(Float)
    start_long = Column(Float)
    stop_lat = Column(Float)
    stop_long = Column(Float)
    # hr_zones_method = Column(String(18))
    hrz_1_hr = Column(Integer)
    hrz_2_hr = Column(Integer)
    hrz_3_hr = Column(Integer)
    hrz_4_hr = Column(Integer)
    hrz_5_hr = Column(Integer)
    hrz_1_time = Column(Time, nullable=False)
    hrz_2_time = Column(Time, nullable=False)
    hrz_3_time = Column(Time, nullable=False)
    hrz_4_time = Column(Time, nullable=False)
    hrz_5_time = Column(Time, nullable=False)

    def __repr__(self):
        return f"<GarminActivity(id='{self.activity_id}', type='{self.type}', start='{self.start_time}')>"


class GarminSleep(Base):
    __tablename__ = "garmin_sleep_sessions"

    day = Column(Date, primary_key=True, index=True)
    start = Column(DateTime)
    end = Column(DateTime)
    total_sleep = Column(Time, nullable=False)
    deep_sleep = Column(Time, nullable=False)
    light_sleep = Column(Time, nullable=False)
    rem_sleep = Column(Time, nullable=False)
    awake = Column(Time, nullable=False)
    avg_spo2 = Column(Float)
    avg_rr = Column(Float)
    avg_stress = Column(Float)
    score = Column(Integer)
    qualifier = Column(String)

    def __repr__(self):
        return f"<GarminSleep(day='{self.day}', total_sleep='{self.total_sleep}')>"
