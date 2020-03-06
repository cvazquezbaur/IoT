/* -*- mode: c; c-basic-offset: 2; indent-tabs-mode: nil; -*-
 * Copyright (C) 2013, 2016 Henner Zeller <h.zeller@acm.org>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation version 2.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http: *gnu.org/licenses/gpl-2.0.txt>
 */

/*
 * We do this in plain C so that we can use designated initializers.
 */
#include "hardware-mapping.h"

#define GPIO_BIT(b) (1<<(b))

struct HardwareMapping matrix_hardware_mappings[] = {
  /*
   * Classic pin-out for Rev-A Raspberry Pi.
   */
  {
    .name          = "classic-pi1",

    /* The Revision-1 and Revision-2 boards have different GPIO mappings
     * on the P1-3 and P1-5. So we use both interpretations.
     * To keep the I2C pins free, we avoid these in later mappings.
     */
    .output_enable = GPIO_BIT(0) | GPIO_BIT(2),
    .clock         = GPIO_BIT(1) | GPIO_BIT(3),
    .strobe        = GPIO_BIT(4),

    .a             = GPIO_BIT(7),
    .b             = GPIO_BIT(8),
    .c             = GPIO_BIT(9),
    .d             = GPIO_BIT(10),

    .p0_r1         = GPIO_BIT(17),
    .p0_g1         = GPIO_BIT(18),
    .p0_b1         = GPIO_BIT(22),
    .p0_r2         = GPIO_BIT(23),
    .p0_g2         = GPIO_BIT(24),
    .p0_b2         = GPIO_BIT(25),
  }
};
