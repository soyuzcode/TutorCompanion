package com.keycode.TutorCompanion.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.keycode.TutorCompanion.model.Review;

@Repository
public interface ReviewRepository
        extends JpaRepository<Review, Long> {

    java.util.List<Review> findByTutor_Id(Long tutorId);

    boolean existsByTutor_IdAndStudent_Id(Long tutorId, Long studentId);
}