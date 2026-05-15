package com.keycode.TutorCompanion.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.keycode.TutorCompanion.model.SessionStudent;
import com.keycode.TutorCompanion.model.SessionStudentId;

@Repository
public interface SessionStudentRepository
        extends JpaRepository<SessionStudent, SessionStudentId> {

}