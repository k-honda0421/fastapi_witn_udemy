from typing import Union

from sqlalchemy.orm import Session
from fastapi import HTTPException

from . import models, schemas


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    ユーザー一覧取得
    """
    return db.query(models.User).offset(skip).limit(limit).all()


def get_rooms(db: Session, skip: int = 0, limit: int = 100):
    """
    会議室一覧取得
    """
    return db.query(models.Room).offset(skip).limit(limit).all()


def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    """
    予約一覧取得
    """
    return db.query(models.Booking).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.User):
    """
    ユーザー登録
    """
    db_user = models.User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_room(db: Session, room: schemas.Room):
    """
    会議室登録
    """
    db_room = models.Room(
        room_name=room.room_name, capacity=room.capacity
    )
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room


def create_booking(db: Session, booking: schemas.Booking):
    """
    予約登録
    """
    # db_booked = db.query(models.Booking).\
    #     filter(models.Booking.room_id == booking.room_id).\
    #     filter(models.Booking.end_datetime > booking.start_datetime).\
    #     filter(models.Booking.start_datetime < booking.end_datetime).\
    #     all()

    # 重複するデータがなければ
    # if len(db_booked) == 0:
    if _is_duplication_bookings_record(
        db=db,
        models=models.Booking,
        received_record=schemas.Booking
    ):
        db_booking = models.Booking(
            user_id=booking.user_id,
            room_id=booking.room_id,
            booked_num=booking.booked_num,
            start_datetime=booking.start_datetime,
            end_datetime=booking.end_datetime
        )
        db.add(db_booking)
        db.commit()
        db.refresh(db_booking)
        return db_booking
    else:
        raise HTTPException(status_code=404, detail="Already booked")


def update_user(db: Session, user: schemas.User):
    target_record = db.query(models.User).get(user.user_id)
    target_record.username = user.username
    db.commit()
    return target_record


def update_room(db: Session, room: schemas.Room):
    target_record = db.query(models.Room).get(room.room_id)
    target_record.room_name = room.room_name
    target_record.capacity = room.capacity
    db.commit()
    return target_record


def update_booking(db: Session, booking: schemas.Booking):
    # db_booked = db.query(models.Booking).\
    #     filter(models.Booking.room_id == booking.room_id).\
    #     filter(models.Booking.end_datetime > booking.start_datetime).\
    #     filter(models.Booking.start_datetime < booking.end_datetime).\
    #     all()

    # 重複するデータがなければ
    # if len(db_booked) == 0:
    if _is_duplication_bookings_record(
        db=db,
        models=models.Booking,
        received_record=schemas.Booking
    ):
        target_record = db.query(models.Booking).get(booking.booking_id)
        target_record.booked_num = booking.booked_num
        target_record.start_datetime = booking.start_datetime
        target_record.end_datetime = booking.end_datetime
        db.commit()
        return target_record
    else:
        raise HTTPException(status_code=404, detail="Already booked")


def _is_duplication_bookings_record(
    db: Session, models: models.Booking, received_record: schemas.Booking
):
    db_booked = db.query(models).\
        filter(models.room_id == received_record.room_id).\
        filter(models.end_datetime > received_record.start_datetime).\
        filter(models.start_datetime < received_record.end_datetime).\
        all()

    if len(db_booked) == 0:
        return True
    else:
        return False
