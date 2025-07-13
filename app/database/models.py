from sqlalchemy import Column, Integer, Float, Date, Time

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
