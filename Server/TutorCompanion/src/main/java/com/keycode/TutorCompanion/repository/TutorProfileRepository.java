package com.keycode.TutorCompanion.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.keycode.TutorCompanion.model.TutorProfile;

@Repository
public interface TutorProfileRepository
        extends JpaRepository<TutorProfile, Long> {
}
