# Topic 40: ffmpeg_whisper_bart_install_toolbox

Number of tickets: 9

## Tickets in this topic:

### 2024051042003622_Ask%20for%20help%20to%20install%20latest%20ffmpeg%20which%20encounters%20an%20error%20using%20spack.md
# Ticket 2024051042003622

 ```markdown
# HPC Support Ticket: Installing Latest ffmpeg without Spack

## Keywords
- ffmpeg
- Spack
- Installation Error
- Configure Options
- Static Builds

## Problem
- User needs to install the latest ffmpeg version (7.0) for a dataset.
- Spack's latest checksummed version is 4.4.1.
- Error occurs during installation of ffmpeg@7.0 using Spack due to unavailable configure options.

## Root Cause
- One of the configure options used in Spack's package.py for ffmpeg has been removed in the 7.0 release.

## Solution
- **Spack Fix**: HPC Admin successfully modified the `package.py` file in Spack-0.19.1 to install ffmpeg-7.0 with Spack's defaults.
- **Alternative**: Recommended using static builds of ffmpeg from the official website, which have been updated to 7.0.

## General Learning
- Always check for changes in configure options when upgrading software versions.
- Modifying Spack's `package.py` can resolve compatibility issues with newer software versions.
- Static builds from official sources can be a quick alternative for installing the latest software versions.
```
---

### 2022101842002381_Using%20ffmpeg.md
# Ticket 2022101842002381

 ```markdown
# HPC-Support Ticket Conversation: Using ffmpeg

## Keywords
- ffmpeg
- installation
- usage
- alex

## Root Cause
User needs to install and use `ffmpeg` on the HPC system `alex`.

## Solution
1. **Installation**:
   - The user should be guided on how to install `ffmpeg` on the HPC system `alex`.
   - This may involve using package managers or compiling from source if necessary.

2. **Usage**:
   - Provide instructions on how to use `ffmpeg` for common tasks.
   - Include examples of commands and any specific configurations required for `alex`.

## General Learnings
- Understanding how to install software on HPC systems.
- Basic usage of `ffmpeg` for video processing tasks.
- Importance of providing clear instructions for software installation and usage on HPC systems.
```
---

### 2024040542002181_Whisper%20is%20failing%20on%20alex2.md
# Ticket 2024040542002181

 ```markdown
# HPC-Support Ticket: Whisper is failing on alex2

## Subject
Whisper is failing on alex2

## User Issue
- **Error Message**: SystemError: initialization of _internal failed without raising an exception
- **Reproduction Steps**:
  1. Allocate a node with `salloc`.
  2. Load a `whisper/20231117` module.
  3. Run `whisper --model large-v2 $FILENAME`.

## Root Cause
- **Environment Conflict**: The user's local environment was conflicting with the module environment. Specifically, the presence of `numba` and `llvmlite` in the user's `.local` directory caused the issue.
- **FFmpeg Issue**: After resolving the environment conflict, the user encountered an issue with `ffmpeg`.

## Solution
- **Step 1**: Delete `numba` and `llvmlite` from the user's `.local` directory.
- **Step 2**: Remove any alias for `ffmpeg` in the user's `.bashrc`.

## Keywords
- Whisper
- SystemError
- Environment Conflict
- numba
- llvmlite
- ffmpeg
- .bashrc

## General Learning
- **Environment Isolation**: Ensure that the user's local environment does not conflict with the module environment.
- **Module Paths**: Modules often prepend paths to ensure the correct environment is used. Conflicts can arise if the user has conflicting paths in their local environment.
- **FFmpeg**: Ensure that the correct version of `ffmpeg` is being used by removing any aliases that might point to a different version.

## Conclusion
The issue was resolved by cleaning up the user's local environment and ensuring that the correct paths were being used. This highlights the importance of maintaining a clean and isolated environment when using HPC modules.
```
---

### 42131317_Kompilieren%20von%20LAMMPS%20auf%20LiMa.md
# Ticket 42131317

 ```markdown
# HPC-Support Ticket: Kompilieren von LAMMPS auf LiMa

## Problem
Der Benutzer konnte LAMMPS auf LiMa nicht kompilieren. Nach dem Laden der Module und dem Hinzufügen von Userpaketen erhielt der Benutzer einen Fehler beim Kompilieren mit dem mkl-Preset.

## Fehlermeldung
```
fft3d.h(212): catastrophic error: could not open source file "fftw.h"
#include "fftw.h"
^
compilation aborted for fft3d.cpp (code 4)
make[1]: *** [fft3d.o] Error 4
```

## Ursache
Der Pfad zur FFTW-Lib im Makefile war falsch gesetzt. Die FFTW-Wrapper müssen manuell erzeugt werden, da LAMMPS die FFTW2-Wrapper benötigt.

## Lösung
1. Verwenden Sie `$(MKL_BASE)` anstelle von `/opt/intel/mkl/10.0.011`.
2. FFTW-Wrapper müssen manuell erzeugt werden.
3. Verwenden Sie die vordefinierten Variablen `$MKL_LIB` (für statisch gelinkte MKL) bzw. `$MKL_SHLIB` (für dynamisch).

## Makefile-Beispiel
```makefile
SHELL = /bin/sh
.IGNORE:
# System-specific settings
CC =            mpiicpc
CCFLAGS =       -O3 -axSSE4.2,SSE4.1,SSSE3,SSE3,SSE2 -DFFT_FFTW -I${MKL_BASE}/include/fftw -DLAMMPS_GZIP -DMPICH_IGNORE_CXX_SEEK -opt-multi-version-aggressive -ansi-alias -fno-alias
DEPFLAGS =      -M
LINK =          mpiicpc
LINKFLAGS =     -O3 -axSSE4.2,SSE4.1,SSSE3,SSE3,SSE2 -opt-multi-version-aggressive -ansi-alias -fno-alias
#USRLIB =        -lstdc++
SYSLIB =        -Wl,-rpath,$(MKL_BASE)/lib/intel64 -L$(MKL_BASE)/lib/intel64 -lmkl_intel_lp64 -lmkl_sequential -lmkl_core
SIZE =          size
# Link rule
$(EXE): $(OBJ)
$(LINK) $(LINKFLAGS) $(OBJ) $(USRLIB) $(SYSLIB) -o $(EXE)
$(SIZE) $(EXE)
# Compilation rules
%.o:%.cpp
$(CC) $(CCFLAGS) -c $<
%.d:%.cpp
$(CC) $(CCFLAGS) $(DEPFLAGS) $< > $@
```

## Zusätzliche Informationen
- Das DXA-Tool (Dislocation Extraction Algorithm) wurde erfolgreich integriert.
- Ein neues Build-Skript wurde erstellt, um die zusätzlichen Pfade zu berücksichtigen.

## Schlüsselwörter
- LAMMPS
- Kompilieren
- FFTW
- MKL
- Makefile
- DXA
- LiMa
```
---

### 2023050242000688_Need%20help%20installing%20ffmpeg%20library%20for%20Whisper%20package%20on%20HPC.md
# Ticket 2023050242000688

 # HPC Support Ticket: Need help installing ffmpeg library for Whisper package on HPC

## Keywords
- Whisper package
- ffmpeg library
- module load
- virtualenv
- pip
- sudo permissions

## Problem
- User needs to install the `ffmpeg` library for the Whisper package.
- Installing `ffmpeg` using `pip` does not work.
- User does not have sudo permissions to install `ffmpeg` system-wide.

## Root Cause
- The Whisper package requires the `ffmpeg` library, which cannot be installed via `pip` and requires system-level installation.
- User lacks sudo permissions to install `ffmpeg` system-wide.

## Solution
- Use the pre-installed Whisper module available on the HPC system.
- Load the Whisper module using the command `module load whisper` on the TinyGPU system.

## Steps to Resolve
1. **Load the Whisper Module:**
   - Open an interactive shell or script.
   - Enter the command: `module load whisper`.

2. **Refer to Documentation:**
   - Review the HPC getting started guide and documentation for more information on using modules.

## General Learnings
- Always check if the required software is already available as a module on the HPC system.
- Use pre-installed modules to avoid permission issues and ensure compatibility with the HPC environment.
- Refer to the HPC documentation for guidance on using modules and other system features.

## Additional Notes
- The user was initially unaware of the pre-installed Whisper module.
- The user faced issues with module commands, indicating a need for better documentation or training on module usage.

## Conclusion
- The issue was resolved by using the pre-installed Whisper module, which includes the necessary `ffmpeg` library.
- The user was advised to refer to the HPC documentation for further assistance.
---

### 2023051742000347_Package%20installation%20in%20Alex.md
# Ticket 2023051742000347

 # HPC Support Ticket: Package Installation in Alex

## Keywords
- Package installation
- ffmpeg
- Alex cluster
- High-quality images
- Python libraries
- $HOME directory

## Problem
- User requested the installation of `ffmpeg` on the Alex cluster to generate high-quality images for simulations.
- Current Python libraries and GIF formats were insufficient for the user's needs.

## Root Cause
- The Alex cluster does not offer `ffmpeg` as a pre-installed package.

## Solution
- HPC Admin advised the user to download and install `ffmpeg` in their `$HOME` directory.
- User confirmed successful installation in their `$HOME` directory.

## General Learnings
- Users can install necessary packages in their `$HOME` directory if they are not available on the cluster.
- HPC Admins provide guidance on self-installation when requested packages are not offered.

## Ticket Status
- Closed: User installed the package themselves.
---

### 2024011242002225_Doubt%20on%20installing%20module%20%28ffmpeg%29%20on%20HPC%20%28Woody%29.md
# Ticket 2024011242002225

 ```markdown
# HPC Support Ticket: Installing ffmpeg on Woody

## Keywords
- ffmpeg
- Woody
- Spack
- Installation
- Permissions

## Problem
- User attempted to install ffmpeg on Woody using the common method (tar + configure + make + make install) but encountered permission issues.
- The module for ffmpeg was not available on the HPC system.

## Root Cause
- The user lacked the necessary permissions to install software directly on the HPC system.

## Solution
- The HPC Admin recommended using Spack, a package manager designed for HPC environments, to install ffmpeg.
- Documentation link provided: [Spack Package Manager](https://hpc.fau.de/systems-services/documentation-instructions/special-applications-and-tips-tricks/spack-package-manager/#collapse_0)

## Outcome
- The user successfully installed ffmpeg using Spack.

## General Learning
- Users should use Spack for installing software on HPC systems to avoid permission issues.
- Documentation and guidelines for using Spack are available on the HPC website.
```
---

### 2023072142002691_%5BTinyX%5D%20Request%20for%20missing%20libraries..md
# Ticket 2023072142002691

 # HPC Support Ticket: Request for Missing Libraries

## Subject
[TinyX] Request for missing libraries.

## User Issue
- User attempting to install BART Toolbox on TinyX node.
- Missing libraries: `libfftw3-dev`, `liblapacke-dev`, `libpng-dev`, `libopenblas-dev`.
- Only `libpng-dev` is installed.

## HPC Admin Response
- Suggested using Singularity containers.
- Provided links to documentation for building containers.
- Mentioned `fftw3` is available as a module.
- Suggested using a Conda environment for Python-based BART Toolbox.
- Provided Conda commands to install missing libraries.

## User Follow-Up
- User had difficulty with Singularity and preferred Conda environment.
- Conda environment setup worked but `lapacke.h` was missing.

## HPC Admin Solution
- Suggested building BART with a contained LAPACKE version.
- Provided instructions to create a file in `bart/Makefiles` with `NOLAPACKE=1`.
- Mentioned additional configuration options in `bart/Makefiles/README.md`.
- Suggested using MKL headers if needed.

## Outcome
- User successfully installed and ran BART Toolbox using the provided workaround.

## Keywords
- BART Toolbox
- Singularity
- Conda environment
- Missing libraries
- LAPACKE
- MKL headers

## Lessons Learned
- Using Singularity containers can be a solution for missing dependencies.
- Conda environments can be used to manage dependencies for Python-based tools.
- BART Toolbox can be built with a contained LAPACKE version if `lapacke.h` is missing.
- MKL headers can be used as an alternative for LAPACKE headers.

## Root Cause
- Missing libraries required for BART Toolbox installation.

## Solution
- Use Singularity containers or Conda environment to manage dependencies.
- Build BART Toolbox with a contained LAPACKE version if `lapacke.h` is missing.
- Use MKL headers as an alternative for LAPACKE headers.
---

### 2023060142001071_Install%20libavcodec-extra-54%20on%20ALex.md
# Ticket 2023060142001071

 ```markdown
# HPC Support Ticket: Install libavcodec-extra-54 on ALex

## Keywords
- ffmpeg
- libavcodec-extra-54
- conda
- compilation
- encoding library

## Problem Description
- User installed ffmpeg in their home directory on ALEX.
- Missing encoding library (libavcodec-extra-54) required for ffmpeg to work properly.
- User requested installation of libavcodec-extra-54, which requires admin rights.

## Root Cause
- User lacks knowledge on compiling software and integrating libraries.
- Missing encoding library causing ffmpeg to malfunction.

## Solutions Provided
1. **Build libx264 and integrate it into ffmpeg build:**
   - User can compile libx264 themselves and integrate it into their ffmpeg build.

2. **Use conda:**
   - Conda provides ffmpeg with Python bindings.
   - Suggested to use the `whisper` module which includes ffmpeg.

## Additional Information
- User referred to a StackOverflow post for guidance.
- HPC Admin suggested using conda as an alternative to manual compilation.
- HPC Admin clarified that libavcodec is part of ffmpeg.

## Conclusion
- User needs guidance on compiling software and integrating libraries.
- Conda is recommended as a simpler solution for managing dependencies.
```
---

