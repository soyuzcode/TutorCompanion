package com.keycode.TutorCompanion.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.keycode.TutorCompanion.model.Subject;

public interface SubjectRepository
        extends JpaRepository<Subject, Long> {

}