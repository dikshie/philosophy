/-
  Week 02: Modal Logic & Kripke Semantics in Lean 4
  Focus: Kripke Frames, Possible Worlds, Box & Diamond, Axiom Correspondence
-/

namespace Week02

-- 1. Definition of Kripke Frame and Model
structure KripkeFrame (W : Type) where
  rel : W → W → Prop

structure KripkeModel (W : Type) extends KripkeFrame W where
  val : String → W → Prop

-- 2. Modal Syntax
inductive Form where
  | atom : String → Form
  | not  : Form → Form
  | and  : Form → Form → Form
  | box  : Form → Form
  deriving Repr

def Form.or (φ ψ : Form) : Form := Form.not (Form.and (Form.not φ) (Form.not ψ))
def Form.diamond (φ : Form) : Form := Form.not (Form.box (Form.not φ))

-- 3. Truth at a World (Semantics)
def eval (M : KripkeModel W) : Form → W → Prop
  | Form.atom p,   w => M.val p w
  | Form.not φ,    w => ¬(eval M φ w)
  | Form.and φ ψ,  w => eval M φ w ∧ eval M ψ w
  | Form.box φ,    w => ∀ v, M.rel w v → eval M φ v

-- 4. Validity in a Frame
def ValidInFrame (F : KripkeFrame W) (φ : Form) : Prop :=
  ∀ (val : String → W → Prop) (w : W),
    let M : KripkeModel W := { rel := F.rel, val := val }
    eval M φ w

-- 5. Correspondence: Axiom T (Box φ → φ) corresponds to Reflexivity
theorem axiom_T_sound_on_reflexive_frame {W : Type} (F : KripkeFrame W)
    (href : ∀ w, F.rel w w) (M : KripkeModel W) (hM : M.rel = F.rel) (φ : Form) (w : W) :
    (∀ v, M.rel w v → eval M φ v) → eval M φ w := by
  intro hbox
  have hrw : M.rel w w := by
    rw [hM]
    exact href w
  exact hbox w hrw

-- 6. Correspondence: Axiom 4 (Box φ → Box Box φ) corresponds to Transitivity
theorem axiom_4_sound_on_transitive_frame {W : Type} (F : KripkeFrame W)
    (htrans : ∀ x y z, F.rel x y → F.rel y z → F.rel x z) (M : KripkeModel W) (hM : M.rel = F.rel)
    (φ : Form) (w : W) :
    (∀ v, M.rel w v → eval M φ v) →
    (∀ u, M.rel w u → ∀ z, M.rel u z → eval M φ z) := by
  intro hbox u hwu z huz
  have hwz : F.rel w z := by
    have h1 : F.rel w u := by rw [←hM]; exact hwu
    have h2 : F.rel u z := by rw [←hM]; exact huz
    exact htrans w u z h1 h2
  have hwz_M : M.rel w z := by rw [hM]; exact hwz
  exact hbox z hwz_M

end Week02
